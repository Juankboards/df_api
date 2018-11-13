from flask import Flask
import json
import dataTransform

app = Flask(__name__)

file = '[{"name": "Maria","lastname": "Matallana", "age": null,"height": 180},{"name": "Juan","lastname": "Ruiz", "age": 28,"height": 180},{"name": "Laura","lastname": "Quintero", "age": 26,"height": 165},{"name": "Markov","lastname": "Ruiz Quintero", "age": 2,"height": 110}]'

@app.route('/')
def home():
    file_df = dataTransform.transformJsonToDf(file)
    return(file_df.to_json())

@app.route('/shape')
def shape():
    file_df = dataTransform.transformJsonToDf(file)
    [rows,columns] = file_df.shape
    shapeInfo = json.dumps({'rows': rows, 'columns': columns})
    return(shapeInfo)

@app.route('/min-values')
def min_values():
    file_df = dataTransform.transformJsonToDf(file)
    min_values_df = file_df.min()

    return(min_values_df.to_json())

@app.route('/max-values')
def max_values():
    file_df = dataTransform.transformJsonToDf(file)
    min_values_df = file_df.max()

    return(min_values_df.to_json())

@app.route('/get-columns/<columns_name>')
def get_columns(columns_name):
    columns = columns_name.split('-')
    try:
        column_df = dataTransform.get_columns(file, columns)
        return(column_df.to_json())
    except:
        return('Invalid Columns')

@app.route('/get-rows/<rows_position>')
def get_rows(rows_position):
    positions = list(map(int, rows_position.split('-')))
    file_df = dataTransform.transformJsonToDf(file)
    rows_df = file_df.reindex(index=positions)

    return(rows_df.to_json())

@app.route('/change-columns-names/<changes>')
def change_columns_names(changes):
    changes = string_to_dict(changes)
    try:
        renamed_df = dataTransform.change_columns_names(file, changes)
        return(renamed_df.to_json())
    except:
        return('Invalid Columns')

@app.route('/drop-columns-na', defaults={'drop_type': 'any'})
@app.route('/drop-columns-na/<drop_type>')
def drop_columns_na(drop_type):
    clean_df = dataTransform.cleanNaColumns(file, drop_type)

    return(clean_df.to_json())


def string_to_dict(str):
    arr = str.split('-')
    dict = {}

    for element in arr:
        [key,val] = element.split('=')
        dict[key] = val

    return dict



if __name__ == '__main__':
    app.run(debug=True)
