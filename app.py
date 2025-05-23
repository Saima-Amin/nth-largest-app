from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = '''
    <h2>Find Nth Largest Number</h2>
    <form method="post">
        Enter numbers (comma-separated):<br>
        <input name="numbers" placeholder="e.g. 5,1,3,9,7"><br><br>
        Enter N:<br>
        <input name="n" type="number"><br><br>
        <input type="submit" value="Find">
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def nth_largest():
    if request.method == 'POST':
        try:
            numbers = list(map(int, request.form['numbers'].split(',')))
            n = int(request.form['n'])
            if n > len(numbers) or n <= 0:
                return f"<h3>Invalid value for N</h3>{form_html}"
            numbers.sort(reverse=True)
            nth = numbers[n-1]
            return f"<h3>{n}-th largest number is: {nth}</h3>{form_html}"
        except:
            return f"<h3>Error: Invalid input</h3>{form_html}"
    return form_html

if __name__ == '__main__':
    app.run()
