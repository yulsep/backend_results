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
        query1 = {
            "$match": {"table.$id": ObjectId(table_id)}
        }
        query_aggregation = {
            '$addFields': {
                'max': {'$max': '$numero_votos'}

            }
        }
        project = {
            '$project': {
                'numero_votos': 1,
                'table': 1,
                'max': 1
            }
        }

        pipeline = [query1, query_aggregation, project]
        return self.query_aggregation(pipeline)

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

    def get_political_party_percentage_votes(self):
        group = {
            '$group': {
                '_id': 'candidates',
                'sum-candidates': {
                    '$sum': '$votes'
                }
            }
        }
        lookup = {
            '$lookup': {
                'from': 'candidates',
                'localField': 'candidates.$id',
                'foreignField': 'parties',
                'as': 'details'
            }
        }
        set = {
            '$set': {
                'details': {
                    '$first': '$candidate'
                }
            }
        }
        lookup1 = {
            '$lookup': {
                'from': 'politicalparty',
                'localField': 'candidates.politicalparty.$id',
                'foreignField': '_id',
                'as': 'political_party'
            }
        }
        set1 = {
            '$set': {
                'political_parys': {
                    '$first': '$politicalparty'
                }
            }
        }
        sort = {
            '$sort': {
                'sum-candidates': -1
            }
        }
        limit = {
            '$limit': 15
        }
        group1 = {
            '$group': {
                '_id': '$politicalparty',
                'candidates_for_parties': {
                    '$count': {}
                }
            }
        }
        add_fields = {
            '$addFields': {
                'porcentaje': {
                    '$sum': [
                        {
                            '$sum': [
                                '$candidates_for_parties', 15
                            ]
                        }, 100
                    ]
                }
            }
        }
        pipeline = [group, lookup, set, lookup1, set1, sort, limit, group1, add_fields]
        return self.query_aggregation(pipeline)



