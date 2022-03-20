import typing as t
import attr

@attr.dataclass
class Person:
    name: str
    age: int
    address: t.Optional[str] = attr.ib(default=None)
    likes: t.Optional[list] = attr.ib(default=None)

some_persons = [Person('Alice', 21, '123 main st'), Person('Bob', 22, '456 other street'), Person('Charlie', 23)]
some_persons2 = [Person(name='Sam', age=28, address='123 Music St', likes=['music','programming', 'video games']), 
                 Person(name='Tina', age=30, address='123 Cool St', likes=['music', 'tv shows', 'Jacques']),
                 Person(name='Jacques', age=None, address=None, likes=['food', 'food', 'more food'])
                 ]

for p in some_persons:
    print(f'{p.name} is {p.age} years old and lives at {p.address}')

for p in some_persons2:
    print(f'{p.name} is {p.age} years old, lives at {p.address}, and likes the following things {p.likes}')

# Alice is 21 years old and lives at 123 main st
# Bob is 22 years old and lives at 456 other street
# Charlie is 23 years old and lives at None
