from sqlalchemy import DateTime, create_engine, Column, Integer, String, Text, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MediaSchema(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    banner = Column(String)
    poster = Column(String)

    def __repr__(self):
        return f"<Usuario(name='{self.name}', banner='{self.banner}' , poster='{self.poster}')>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "banner": self.banner,
            "poster": self.poster,
        }
    
class MediaContentSchema(Base):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True, autoincrement=True)
    media_id = Column(Integer)
    ano_de_lancamento = Column(Integer)
    classificacao_etaria = Column(String)
    plataformas_streaming = Column(String)
    numero_de_episodios = Column(Integer)
    sinopse = Column(Text)
    genero = Column(String)
    temporada = Column(Integer)
    ultima_atualizacao = Column(DateTime, default=func.now(), onupdate=func.now())
    nota=Column(Integer)

    def __repr__(self):
        return (
            f"<Media_Content(id='{self.id}', media_id='{self.media_id}', "
            f"ano_de_lancamento='{self.ano_de_lancamento}', classificacao_etaria='{self.classificacao_etaria}', "
            f"plataformas_streaming='{self.plataformas_streaming}', "
            f"numero_de_episodios='{self.numero_de_episodios}', sinopse='{self.sinopse}', "
            f"genero='{self.genero}', temporada='{self.temporada}'), ultima_atualizacao='{self.ultima_atualizacao}', nota='{self.nota}'/>"

        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "media_id": self.media_id,
            "ano_de_lancamento": self.ano_de_lancamento,
            "classificacao_etaria": self.classificacao_etaria,
            "plataformas_streaming": self.plataformas_streaming,
            "numero_de_episodios": self.numero_de_episodios,
            "sinopse": self.sinopse,
            "genero": self.genero,
            "temporada": self.temporada,
            "ultima_atualizacao": self.ultima_atualizacao,
            "nota": self.nota,
        }
    
# Criação de uma base de dados
def create_database():
    engine = create_engine('sqlite:///media.db', echo=True)
    Base.metadata.create_all(engine)
    return engine

# Criação de uma sessão
def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def main():
    engine = create_database()
    session = create_session(engine)

    # Adicionando dados de exemplo
    novo_media = MediaSchema(name='Example Movie', banner='example_banner.jpg', poster='example_poster.jpg')
    session.add(novo_media)
    session.commit()

    novo_media_content = MediaContentSchema(
        media_id=novo_media.id,
        ano_de_lancamento=2021,
        classificacao_etaria='PG-13',
        plataformas_streaming='Netflix, Amazon Prime',
        numero_de_episodios=10,
        sinopse='A thrilling adventure movie.',
        genero='Adventure',
        temporada=1
    )
    session.add(novo_media_content)
    session.commit()

    # Consultando e imprimindo os dados
    for media in session.query(MediaSchema).all():
        print(media)
    for content in session.query(MediaContentSchema).all():
        print(content)

if __name__ == "__main__":
    main()
