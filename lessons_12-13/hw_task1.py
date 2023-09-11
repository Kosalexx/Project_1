from typing import Any


class Vector():
    def __init__(self,
                 point1: tuple[float, float],
                 point2: tuple[float, float]) -> None:
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2

    def length(self) -> float:
        result: float = round(
            ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5, 2)
        return result

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            raise ValueError("The second object must be Vector.")
        return self.length() == other.length()

    def __ne__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            raise ValueError("The second object must be Vector.")
        return self.length() != other.length()

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            raise ValueError("The second object must be Vector.")
        return self.length() > other.length()

    def __ge__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            raise ValueError("The second object must be Vector.")
        return self.length() >= other.length()


vec1 = Vector((2, 3), (4, 5))
vec2 = Vector((3, 1), (8, 5))
vec3 = Vector((2, 3), (4, 5))
vec4 = Vector((3.5, 7), (3.5, 9))

print(vec1.length())
print(vec2.length())
print(vec3.length())
print(vec4.length())
print(vec1 == vec2)
print(vec3 != vec2)
print(vec1 < vec4)
print(vec1 > vec4)
print(vec4 <= vec2)
print(vec4 >= vec2)
