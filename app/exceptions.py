from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"

class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect email or password"

class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token has expired"

class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "The token is missing"

class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorrect token format"

class UserIsNotPresentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ""


# UserAlreadyExistsException = HTTPException(
#     status_code=status.HTTP_409_CONFLICT,
#     detail="User already exists",
# )

# IncorrectEmailOrPasswordException = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail="Incorrect email or password",
# )

# TokenExpiredException = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail="The token has expired",
# )

# TokenAbsentException = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail="The token is missing",
# )

# IncorrectTokenFormatException = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail="Incorret token format",
# )

# UserIsNotPresentException = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
# )
