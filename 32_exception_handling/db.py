import sqlite3

class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass


def blog_lst_to_json(item):
    '''
    Converts list data to dictionary to return as json
    '''
    return { 
        'id': item[0],
        'published': item[1],
        'title': item[2],
        'content': item[3],
        'public': bool(item[4])
         }

def fetch_blogs():
    con = sqlite3.connect('application.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM blogs where public=1')

    result = list(map(blog_lst_to_json,cur.fetchall()))

    con.close()

    return result


def fetch_blog(id: str):
    try:
        con = sqlite3.connect('application.db')
        cur = con.cursor()

        cur.execute(f"SELECT * FROM blogs where id='{id}'")
        result = cur.fetchone()

        if result is None:
            raise NotFoundError(f'Unable to find the blog with id = {id}.')

        data = blog_lst_to_json(result)
        if not data['public']:
            raise NotAuthorizedError(f" You're not authorized to acces this blog")

        return data
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundError(f'Unable to find the blog with id = {id}.')
    # Because of the exception, we're not closing the database anymore, so, execute this code anyways
    finally:
        # regars if there's an exception or not, execute this part
        con.close()

