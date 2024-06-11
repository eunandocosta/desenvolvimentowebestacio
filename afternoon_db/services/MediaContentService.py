from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List, Optional

from schemas.Schema import MediaContentSchema

class MediaContentService:
    def __init__(self, session: Session):
        self.session = session

    def create_media_content(self, media_id: int, ano_de_lancamento: int, classificacao_etaria: str, plataformas_streaming: str, numero_de_episodios: int, sinopse: str, genero: str, temporada: int, nota:int) -> MediaContentSchema:
        new_media_content = MediaContentSchema(
            media_id=media_id,
            ano_de_lancamento=ano_de_lancamento,
            classificacao_etaria=classificacao_etaria,
            plataformas_streaming=plataformas_streaming,
            numero_de_episodios=numero_de_episodios,
            sinopse=sinopse,
            genero=genero,
            temporada=temporada,
            nota=nota
        )
        self.session.add(new_media_content)
        self.session.commit()
        return new_media_content

    def get_all_media_content(self) -> List[MediaContentSchema]:
        return self.session.query(MediaContentSchema).all()

    def get_media_content_by_id(self, media_content_id: int) -> Optional[MediaContentSchema]:
        try:
            return self.session.query(MediaContentSchema).filter(MediaContentSchema.id == media_content_id).one()
        except NoResultFound:
            return None

    def update_media_content(self, media_content_id: int, media_id: Optional[int] = None, ano_de_lancamento: Optional[int] = None, classificacao_etaria: Optional[str] = None, plataformas_streaming: Optional[str] = None, numero_de_episodios: Optional[int] = None, sinopse: Optional[str] = None, genero: Optional[str] = None, temporada: Optional[int] = None) -> Optional[MediaContentSchema]:
        media_content = self.get_media_content_by_id(media_content_id)
        if media_content:
            if media_id:
                media_content.media_id = media_id
            if ano_de_lancamento:
                media_content.ano_de_lancamento = ano_de_lancamento
            if classificacao_etaria:
                media_content.classificacao_etaria = classificacao_etaria
            if plataformas_streaming:
                media_content.plataformas_streaming = plataformas_streaming
            if numero_de_episodios:
                media_content.numero_de_episodios = numero_de_episodios
            if sinopse:
                media_content.sinopse = sinopse
            if genero:
                media_content.genero = genero
            if temporada:
                media_content.temporada = temporada
            self.session.commit()
        return media_content

    def delete_media_content(self, media_content_id: int) -> bool:
        media_content = self.get_media_content_by_id(media_content_id)
        if media_content:
            self.session.delete(media_content)
            self.session.commit()
            return True
        return False
