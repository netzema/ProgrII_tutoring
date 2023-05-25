# %% Exercise 1

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
# %%
# Create an in-memory SQLite database
engine = create_engine('sqlite:///mydatabase.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    dob = Column(Date)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Establish a connection and create a session
Session = sessionmaker(bind=engine)
session = Session()

# %% Exercise 2
# Insert sample User objects
user1 = User(name='John', email='john@example.com', dob=date(1997, 1, 1))
user2 = User(name='Jane', email='jane@example.com', dob=date(2001, 1, 1))
user3 = User(name='Hannes', email='hannes@example.com', dob=date(1999, 1, 1))

session.add_all([user1, user2, user3])
session.commit()

# Query all users
all_users = session.query(User).all()

# Query users with names starting with 'J'
j_users = session.query(User).filter(User.name.like('J%')).all()

# %% Exercise 3
# Update the email address of a specific user
user = session.query(User).filter_by(name='John').first()
user.email = 'newemail@example.com'
session.commit()

# Delete a user from the database
user = session.query(User).filter_by(name='Hannes').first()
session.delete(user)
session.commit()

# %% Exercise 4

from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='posts')

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Insert sample Post objects for a user
post1 = Post(title='Post 1', content='Content 1', user=user1)
post2 = Post(title='Post 2 SQL', content='Content 2', user=user1)
post3 = Post(title='Post 3', content='Content 3', user=user2)

session.add_all([post1, post2, post3])
session.commit()

# Retrieve all posts by a specific user
user = session.query(User).filter_by(name='John').first()
user_posts = user.posts

# %% Exercise 5
from sqlalchemy import func

# Retrieve users with the highest number of posts
max_posts = session.query(func.count(Post.id)).join(User).group_by(User.id).order_by(func.count(Post.id).desc()).first()
users_with_max_posts = session.query(User).join(Post).group_by(User.id).having(func.count(Post.id) == max_posts[0]).all()

# Retrieve the count of posts for each user
post_counts = session.query(User.name, func.count(Post.id)).join(Post).group_by(User.id).all()

# Retrieve users who have a post with a specific keyword in the title
keyword = 'SQL'
users_with_keyword_posts = session.query(User).join(Post).filter(Post.title.like(f'%{keyword}%')).all()

# %%
# Example: Query all users from the 'users' table
users = session.query(User).all()
for user in users:
    print(user.name, user.email)
# %% Exercise 6
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='addresses')

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Insert sample Address objects for a user
address1 = Address(street='123 Main St', city='City A', user=user1)
address2 = Address(street='456 Elm St', city='City B', user=user1)

session.add_all([address1, address2])
session.commit()

# Query a user and retrieve all their addresses
user = session.query(User).filter_by(name='John').first()
user_addresses = user.addresses
# %% Exercise 7
from sqlalchemy import func

# Calculate the total number of users in the database
total_users = session.query(func.count(User.id)).scalar()

# Find the user(s) with the maximum number of addresses
max_address_count = session.query(func.count(Address.id)).join(User).group_by(User.id).order_by(func.count(Address.id).desc()).first()
users_with_max_addresses = session.query(User).join(Address).group_by(User.id).having(func.count(Address.id) == max_address_count[0]).all()

# %% Exercise 8
# Retrieve the top 5 users with the highest user IDs
top_users = session.query(User).order_by(User.id.desc()).limit(5).all()

# Retrieve users in alphabetical order by their names
alphabetical_users = session.query(User).order_by(User.name).all()

# Retrieve the youngest user based on their birthdate
youngest_user = session.query(User).order_by(User.dob.asc()).first()
# %% Exercise 9
# Retrieve users whose names contain the letter 'a'
users_with_a = session.query(User).filter(User.name.like('%a%')).all()

# Retrieve users who have at least two addresses
users_with_multiple_addresses = session.query(User).join(Address).group_by(User.id).having(func.count(Address.id) >= 2).all()

# Retrieve users born between a specific range of dates
start_date = date(1990, 1, 1)
end_date = date(2000, 12, 31)
users_in_date_range = session.query(User).filter(User.dob.between(start_date, end_date)).all()
# %% Exercise 10
# Update the street name of a specific address
address = session.query(Address).filter_by(id=1).first()
address.street = 'New Street'
session.commit()

# Delete an address from the database
address = session.query(Address).filter_by(id=2).first()
session.delete(address)
session.commit()
# %% Exercise 11
# Retrieve users and their corresponding addresses using an explicit join
users_with_addresses = session.query(User, Address).join(Address).all()

# Retrieve users who have at least one address in a specific city
city = 'City A'
users_in_city = session.query(User).join(Address).filter(Address.city == city).all()
# %%
