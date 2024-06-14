class UrlConnection:

    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'st_user'
    DB_PASS: str = '122333'
    DB_NAME: str = 'st'

    def database_url_psycopg(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = UrlConnection()
