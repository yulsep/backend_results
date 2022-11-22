from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class ReportRepository(InterfaceRepository[Vote]):

    # get reports by candidates
    def get_votes_by_candidate(self, id_candidate):
        theQuery = {"candidate.$id": ObjectId(id_candidate)}
        return self.query(theQuery)

    def get_vote_in_candidate(self):
        query_aggregation = {
            '$addFields': {
                'max': {'$max': '$numero_votos'}
            }
        }
        project = {
            '$project': {
                'table_number': 1,
                'numero_votos': 1,
                'candidate': 1,
                'table': 1,
                'max': 1
            }
        }
        pipeline = [query_aggregation, project]
        return self.query_aggregation(pipeline)

    # get reports by tables

    def get_votes_by_table(self) -> list:
        query_lookup = {
            '$lookup': {
                'from': 'table',
                'localField': 'table.$id',
                'foreignField': '_id',
                'as': 'details'
            }
        }
        query_unwind = {
            '$unwind': '$details'
        }
        query_group = {
            '$group': {
                '_id': '$details',
                'count': {
                    '$sum': 1
                }
            }
        }
        query_add_fields = {
            '$addFields': {
                'table_number': '$_id.table_number',
                'registered_ids': '$_id.registered_ids',
                '_id': '$_id._id'
            }
        }
        query_sort = {
            '$sort': {
                'count': 1
            }
        }
        pipeline = [query_lookup, query_unwind, query_group, query_add_fields, query_sort]
        return self.query_aggregation(pipeline)

    def get_votes_in_table(self, table_id: str):
        pipeline = {"table.$id": ObjectId(table_id)}
        return self.query(pipeline)

    # get reports by political party

    def get_votes_by_political_party(self) -> list:
        query_aggregation = {
            '$addFields': {
                'max': {'$max': '$numero_votos'}
            }
        }
        project = {
            '$project': {
                'candidate': 1,
                'table': 1,
                'max': 1
            }
        }

        pipeline = [query_aggregation, project]
        return self.query_aggregation(pipeline)

    def get_votes_in_political_party(self, political_party_id: str) -> list:
        pipeline = {"politicalparty.$id": ObjectId(political_party_id)}
        return self.query(pipeline)
