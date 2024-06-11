from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List, Optional

from schemas.Schema import MediaSchema

class MediaService:
    def __init__(self, session: Session):
        self.session = session

    def create_mediaSchema(self, name: str, banner: str, poster: str) -> MediaSchema:
        new_mediaSchema = MediaSchema(name=name, banner=banner, poster=poster)
        self.session.add(new_mediaSchema)
        self.session.commit()
        return new_mediaSchema

    def get_all_mediaSchema(self) -> List[MediaSchema]:
        return self.session.query(MediaSchema).all()

    def get_mediaSchema_by_id(self, mediaSchema_id: int) -> Optional[MediaSchema]:
        try:
            return self.session.query(MediaSchema).filter(MediaSchema.id == mediaSchema_id).one()
        except NoResultFound:
            return None

    def update_mediaSchema(self, mediaSchema_id: int, name: Optional[str] = None, banner: Optional[str] = None, poster: Optional[str] = None) -> Optional[MediaSchema]:
        mediaSchema = self.get_mediaSchema_by_id(mediaSchema_id)
        if mediaSchema:
            if name:
                mediaSchema.name = name
            if banner:
                mediaSchema.banner = banner
            if poster:
                mediaSchema.poster = poster
            self.session.commit()
        return mediaSchema

    def delete_mediaSchema(self, mediaSchema_id: int) -> bool:
        mediaSchema = self.get_mediaSchema_by_id(mediaSchema_id)
        if mediaSchema:
            self.session.delete(mediaSchema)
            self.session.commit()
            return True
        return False
