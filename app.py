import os
from flask import Flask, request, jsonify
import db.init_db

app = Flask(__name__)

@app.route('/list-missing-people', methods=['GET'])
def consultar_pessoas():
    conn = db.init_db.getConnection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tb_pessoa_desaparecida;')
    missing_people = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(missing_people)

@app.route('/insert-missing-person', methods=['POST'])
def insert_missing_person(response):
    request_data = request.get_json()

    conn = db.init_db.getConnection()
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

    conn = db.init_db.getConnection()
    cur = conn.cursor()
    cur.execute(f'DELETE FROM tb_pessoa_desaparecida WHERE id_p_desaparecida = {request_data["person_id"]};')
    conn.commit()
    cur.close()
    conn.close()

    return "Done"

@app.route('/alter-missing-person', methods=['PUT'])
def alter_missing_person(res):
    request_data = request.get_json()

    conn = db.init_db.getConnection()
    cur = conn.cursor()
    cur.execute(f"UPDATE tb_pessoa_desaparecida "
                f"SET {request_data['column']} = '{request_data['value']}' "
                f"WHERE id_p_desaparecida = {request_data['person_id']};")
    conn.commit()
    cur.close()
    conn.close()

    return "Done"


port = int(os.environ.get("PORT", 5000)) 
app.run(debug=False, host='0.0.0.0', port=port)
