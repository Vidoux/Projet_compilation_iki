import tempfile
import subprocess

# Fonction pour exécuter un fichier Iki et récupérer le résultat
def run_iki_file(file_path):
    process = subprocess.Popen(['python', 'iki_complete_check.py', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return output.strip() + error.strip()  # Concaténer les sorties standard et d'erreur

# Fonction pour comparer le résultat obtenu avec le résultat attendu
def compare_results(file_path, expected_result):
    actual_result = run_iki_file(file_path)
    if actual_result == expected_result:
        print(f"Test passed: {file_path}")
        print("Expected:", expected_result)
        print("Actual:", actual_result)
    else:
        print(f"Test failed: {file_path}")
        print("Expected:", expected_result)
        print("Actual:", actual_result)
    print("-------------------------")

# Liste des tests
tests = [
    {
        'code': 'var x: int; x = 10;',
        'expected_result': 'Code conforme, prêt à être compilé'
    },
    {
        'code': 'var x: int; var x: int;',
        'expected_result': 'Variable \'x\' already declared.'
    },
    {
        'code': 'var x: int; x = true;',
        'expected_result': 'Type mismatch in assignment: variable \'x\' expects type \'TYPE_INT\', but found type \'TYPE_BOOL\'.'
    },
     {
        'code': 'var x: int; x = y;',
        'expected_result': 'Variable \'y\' not declared.'
    },
    {
        'code': 'var x: int; var y: bool; x = y;',
        'expected_result': 'Type mismatch in assignment: variable \'x\' expects type \'TYPE_INT\', but found type \'TYPE_BOOL\'.'
    },
    {
        'code': 'var x: int; x = 10 + true;',
        'expected_result': 'Type mismatch in binary operator \'+\'.'
    },
    {
        'code': 'var x: int; x = 10 - true;',
        'expected_result': 'Type mismatch in binary operator \'-\'.'
    },
    {
        'code': 'var x: int; x = 10 * true;',
        'expected_result': 'Type mismatch in binary operator \'*\'.'
    },
    {
        'code': 'var x: int; x = 10 / true;',
        'expected_result': 'Type mismatch in binary operator \'/\'.'
    },
    {
        'code': 'var x: bool; x = true;',
        'expected_result': 'Code conforme, prêt à être compilé'
    },
    {
        'code': 'var x: bool; x = 10;',
        'expected_result': 'Type mismatch in assignment: variable \'x\' expects type \'TYPE_BOOL\', but found type \'TYPE_INT\'.'
    }
]

# Boucle sur les tests
for i, test in enumerate(tests):
    # Créer un fichier temporaire
    with tempfile.NamedTemporaryFile(suffix='.iki', delete=False) as temp_file:
        temp_file.write(test['code'].encode())
        temp_file.close()

        # Exécuter le test
        compare_results(temp_file.name, test['expected_result'])
