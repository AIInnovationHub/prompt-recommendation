from domain.user_repository import UserRepository

user_db_file = 'user.db'
prompt_db_file = 'prompt.db'
user_repository = UserRepository(user_db_file)
prompt_repository = PromptRepository(prompt_db_file)