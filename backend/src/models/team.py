from sqlalchemy_serializer import SerializerMixin
from models import db

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    registration = db.Column(db.Boolean)

    #foriegn key
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'))
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'))

    # relationships
    players = db.relationship('Player', back_populates = 'team')
    coaches = db.relationship('Coach', back_populates = 'team')
    permits = db.relationship('Permit', back_populates = 'team')
    school = db.relationship('School', back_populates = 'teams')
    division = db.relationship('Division', back_populates = 'teams')

    # serialize rules
    serialize_rules = ['-players.team']
    serialize_rules = ['-coaches.team']
    serialize_rules = ['-permits.team']
    serialize_rules = ['-school.teams']
    serialize_rules = ['-division.teams']

    # validations
    

    def __repr__(self):
        return f"<Team {self.name} >"