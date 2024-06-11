from flask import Blueprint, request, jsonify, g
from services.MediaContentService import MediaContentService

media_content_blueprint = Blueprint('media_content', __name__)

@media_content_blueprint.route('/', methods=['POST'])
def create_media_content():
    data = request.get_json()
    service = MediaContentService(g.session)
    new_media_content = service.create_media_content(
        media_id=data.get('media_id'),
        ano_de_lancamento=data.get('ano_de_lancamento'),
        classificacao_etaria=data.get('classificacao_etaria'),
        plataformas_streaming=data.get('plataformas_streaming'),
        numero_de_episodios=data.get('numero_de_episodios'),
        sinopse=data.get('sinopse'),
        genero=data.get('genero'),
        temporada=data.get('temporada'),
        nota=data.get('nota'),
    )
    return jsonify(new_media_content.to_dict()), 201

@media_content_blueprint.route('/', methods=['GET'])
def get_all_media_content():
    service = MediaContentService(g.session)
    media_content_list = service.get_all_media_content()
    result = [media_content.to_dict() for media_content in media_content_list]
    return jsonify(result)

@media_content_blueprint.route('/<int:media_content_id>', methods=['GET'])
def get_media_content_by_id(media_content_id):
    service = MediaContentService(g.session)
    media_content = service.get_media_content_by_id(media_content_id)
    if media_content:
        return jsonify(media_content.to_dict()), 200
    return jsonify({'message': 'Media content not found'}), 404

@media_content_blueprint.route('/<int:media_content_id>', methods=['PUT'])
def update_media_content(media_content_id):
    data = request.get_json()
    service = MediaContentService(g.session)
    updated_media_content = service.update_media_content(
        media_content_id,
        media_id=data.get('media_id'),
        ano_de_lancamento=data.get('ano_de_lancamento'),
        classificacao_etaria=data.get('classificacao_etaria'),
        plataformas_streaming=data.get('plataformas_streaming'),
        numero_de_episodios=data.get('numero_de_episodios'),
        sinopse=data.get('sinopse'),
        genero=data.get('genero'),
        temporada=data.get('temporada'),
        nota=data.get('nota')
    )
    if updated_media_content:
        return jsonify(updated_media_content.to_dict()), 200
    return jsonify({'message': 'Media content not found'}), 404

@media_content_blueprint.route('/<int:media_content_id>', methods=['DELETE'])
def delete_media_content(media_content_id):
    service = MediaContentService(g.session)
    success = service.delete_media_content(media_content_id)
    if success:
        return jsonify({'message': 'Media content deleted'}), 200
    return jsonify({'message': 'Media content not found'}), 404
