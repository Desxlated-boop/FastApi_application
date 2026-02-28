from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int
    
    @property
    def is_adult(self) -> bool:
        return self.age >= 18

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    
    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, v: str) -> str:
        forbidden_words = ['кринж', 'рофл', 'вайб']
        v_lower = v.lower()
        for word in forbidden_words:
            if word in v_lower:
                raise ValueError('Использование недопустимых слов')
        return v