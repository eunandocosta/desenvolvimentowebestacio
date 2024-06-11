from flask import Blueprint, request, jsonify, g
from services.MediaService import MediaService

media_blueprint = Blueprint('media', __name__)

@media_blueprint.route('/', methods=['GET'])
def media_home():
    return "Media home", 201

@media_blueprint.route('/media_post', methods=['POST'])
def create_media():
    data = request.get_json()
    service = MediaService(g.session)
    new_media = service.create_mediaSchema(
        name=data.get('name'),
        banner=data.get('banner'),
        poster=data.get('poster')
    )
    return jsonify(new_media.to_dict()), 201

@media_blueprint.route('/media_get', methods=['GET'])
def get_all_media():
    service = MediaService(g.session)
    media_list = service.get_all_mediaSchema()
    return jsonify([media.to_dict() for media in media_list]), 200

@media_blueprint.route('/<int:media_id>', methods=['GET'])
def get_media_by_id(media_id):
    service = MediaService(g.session)
    media = service.get_mediaSchema_by_id(media_id)
    if media:
        return jsonify(media.to_dict()), 200
    return jsonify({'message': 'Media not found'}), 404

@media_blueprint.route('/<int:media_id>', methods=['PUT'])
def update_media(media_id):
    data = request.get_json()
    service = MediaService(g.session)
    updated_media = service.update_mediaSchema(
        media_id,
        name=data.get('name'),
        banner=data.get('banner'),
        poster=data.get('poster')
    )
    if updated_media:
        return jsonify(updated_media.to_dict()), 200
    return jsonify({'message': 'Media not found'}), 404

@media_blueprint.route('/<int:media_id>', methods=['DELETE'])
def delete_media(media_id):
    service = MediaService(g.session)
    success = service.delete_mediaSchema(media_id)
    if success:
        return jsonify({'message': 'Media deleted'}), 200
    return jsonify({'message': 'Media not found'}), 404
