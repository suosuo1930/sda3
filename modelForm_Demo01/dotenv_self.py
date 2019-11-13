import os
import dotenv
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelForm_Demo01.settings')
    import django
    django.setup()


    from dotenv import load_dotenv
    from pathlib import Path
    env_path = Path("./modelForm_Demo01/.env")
    # print('env_path=', env_path)

    # load_dotenv(dotenv_path= env_path)
    load_dotenv()
    print(os.getenv("SHIWEI_HOME"))
    # courseList = eval(os.getenv("courseList"))
    # print(type(courseList))
    # print(courseList[0])

