#%% Set Up
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date
# %% Exercise 1
folder_path = "/path/to/folder with space"
file_path = os.path.join(folder_path, "mydatabase.db")
engine = create_engine(f"sqlite:///{file_path}")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    dob = Column(Date)

# Create table if it does not exist
Base.metadata.create_all(engine)

# Establish connection, create session
Session = sessionmaker(bind=engine)
session = Session()
# %% Exercise 2
user1 = User(name="John", email="john@example.com", dob=date(1997, 1, 1))
user2 = User(name="Jane", email="jane@example.com", dob=date(2001, 1, 1))
user3 = User(name="Hannes", email="hannes@example.com", dob=date(1999, 1, 1))

session.add_all([user1, user2, user3])
session.commit()
# %%
# Query users
all_users = session.query(User).all()
j_users = session.query(User).filter(User.name.like("J%")).all()
# %% Exercise 3
user = session.query(User).filter_by(name="John").first()
user.email = "newemail@example.com"
session.commit()

user = session.query(User).filter_by(name="Hannes").first()
session.delete(user)
session.commit()
# %% Exercise 4

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="posts")

# Create table if it does not exist already
Post.metadata.create_all(engine)

# Insert sample Post objects for a user
post1 = Post(title='Post 1', content='Content 1', user=user1)
post2 = Post(title='Post 2 SQL', content='Content 2', user=user1)
post3 = Post(title='Post 3', content='Content 3', user=user2)

session.add_all([post1, post2, post3])
session.commit()

# Retrieve all posts by a specific user
user = session.query(User).filter_by(name="John").first()
user_posts = user.posts
# %% Exercise 5

# Retrieve users with the highest number of posts
max_posts = session.query(func.count(Post.id)).join(User).group_by(User.id).order_by(func.count(Post.id).desc()).first()
users_with_max_posts = session.query(User).join(Post).group_by(User.id).having(func.count(Post.id) == max_posts[0]).all()

# Retrieve the count of posts for each user
post_counts = session.query(User.name, func.count(Post.id)).join(Post).group_by(User.id).all()

# Retrieve users who have a post with a specific keyword in the title
keyword = "SQL"
users_with_keyword_posts = session.query(User).join(Post).filter(Post.title.like(f"%{keyword}%")).all()
# %%
