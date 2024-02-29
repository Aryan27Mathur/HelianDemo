from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Email %r>' % self.address

@app.route('/email', methods=['POST'])
def add_email():
    data = request.json
    if 'address' not in data:
        return jsonify({'error': 'Missing address parameter'}), 400

    email_address = data['address']
    if Email.query.filter_by(address=email_address).first():
        return jsonify({'error': 'Email address already exists'}), 400

    new_email = Email(address=email_address)
    db.session.add(new_email)
    db.session.commit()

    return jsonify({'message': 'Email added successfully'}), 201

@app.route('/getemails', methods=['GET'])
def get_emails():
    emails = Email.query.all()
    email_list = [email.address for email in emails]
    return jsonify({'emails': email_list})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
