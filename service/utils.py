import base64




def decode_encoded_file_path(encoded_file_path: str):
    """
    decode encoded file provided
    """
    decoded_file = base64.b64decode(encoded_file_path)
    with open("service_account_key.json", 'w', encoding="UTF-8") as j_file:
        j_file.write(decoded_file.decode("utf-8"))


# from fastapi import HTTPException
# from fastapi.security import JSONResponse
# from firebase_admin import auth
# from firebase_admin.auth import InvalidIdTokenError
# from hashids import Hashids  # type: ignore
# from passlib.context import CryptContext
# from sqlalchemy.orm import Session

# from models.users import User
# from schemas.settings import settings

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# setting = settings()
# hashid = Hashids(salt=setting.hash_salt, min_length=10)


# def set_user_cookie(resp: JSONResponse, access_token: str) -> None:
#     """set user token in the browser cookie"""
#     resp.set_cookie("access_token", access_token)


# def verify_id_token(token: str):
#     """verify user provided token..."""
#     cred = HTTPException(
#         status_code=401,
#         detail="Invalid authentication credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         decode_token = auth.verify_id_token(token)
#         print(decode_token)
#         return decode_token
#     except InvalidIdTokenError:
#         raise cred


# def hash_password(raw_pass: str) -> str:
#     return pwd_context.hash(raw_pass)


# def verify_hash_password(raw_pass: str, hashed_password: str) -> bool:
#     return pwd_context.verify(raw_pass, hashed_password)


# def authenticate_user(db: Session, email: str, password: str) -> User | None:
#     """
#     Authenticate user with both email and password
#     """
#     user = db.query(User).filter(User.email == email).first()
#     if not user:
#         return None
#     if not verify_hash_password(password, user.password):
#         return None
#     return user


# def hash_id(user_id: int) -> str:
#     """
#     hash user id
#     """
#     return hashid.encode(user_id)


# def un_hash_id(hashed_val: str) -> str:
#     """
#     decode user id
#     """
#     return hashid.decode(hashed_val)
