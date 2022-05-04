from app import app
from flask import render_template
import psycopg2

'''def getConnection():
    conn = psycopg2.connect(host='ec2-3-230-122-20.compute-1.amazonaws.com',
                            database='d16l4f8fojv0d3',
                            user='dgsitkfgyzkuev',
                            password='5bab5efdefe1923873c82735d8dcc559c38c4fde5d6b4d6666cc0b920754079b')
    return conn'''


@app.route('/<user>')
@app.route('/', defaults={"user": None})
def helloworld(user):
    return render_template('index.html',user=user)



'''@app.route('/list-missing-people', methods=['GET'])
def consultar_pessoas():
    conn = getConnection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tb_pessoa_desaparecida;')
    missing_people = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(missing_people)

@app.route('/insert-missing-person', methods=['POST'])
def insert_missing_person(response):
    request_data = request.get_json()

    conn = getConnection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO tb_pessoa_desaparecida "
                f"(nome, data_nascimento, local_desaparecimento, detalhes_desaparecimento) "
                f"VALUES ('{request_data['nome']}', "
                f"'{request_data['data_nascimento']}', "
                f"'{request_data['local_desaparecimento']}', "
                f"'{request_data['detalhes_desaparecimento']}');")
    conn.commit()
    cur.close()
    conn.close()

    return "Done"


@app.route('/delete-missing-person', methods=['DELETE'])
def delete_missing_person():
    request_data = request.get_json()

    conn = getConnection()
    cur = conn.cursor()
    cur.execute(f'DELETE FROM tb_pessoa_desaparecida WHERE id_p_desaparecida = {request_data["person_id"]};')
    conn.commit()
    cur.close()
    conn.close()

    return "Done"

@app.route('/alter-missing-person', methods=['PUT'])
def alter_missing_person(res):
    request_data = request.get_json()

    conn = getConnection()
    cur = conn.cursor()
    cur.execute(f"UPDATE tb_pessoa_desaparecida "
                f"SET {request_data['column']} = '{request_data['value']}' "
                f"WHERE id_p_desaparecida = {request_data['person_id']};")
    conn.commit()
    cur.close()
    conn.close()

    return "Done"
    '''