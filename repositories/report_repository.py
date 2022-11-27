from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class ReportRepository(InterfaceRepository[Vote]):

    # get reports by candidates
    def get_votes_in_candidate(self, id_candidate):
        theQuery = {"candidate.$id": ObjectId(id_candidate)}
        return self.query(theQuery)

    def get_vote_by_candidate(self):
        query_aggregation = {
            '$addFields': {
                'max': {'$max': '$numero_votos'}

            }
        }
        project = {
            '$project': {
                'table_number': 1,
                'votos_registrados': 1,
                'candidate': 1,
                'table': 1,
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
                'votos_registrados': '$_id.votos_registrados',
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
        theQuery = {"table.$id": ObjectId(table_id)}
        return self.query(theQuery)


    # get reports by political party

    def get_votes_by_political_party(self) -> list:
        lookup = {
            '$lookup': {
                'from': 'candidates',
                'localField': 'candidates.$id',
                'foreignField': 'parties_id',
                'as': 'candidates_info'
            }

        }
        unwind = {

                '$unwind': '$candidates_info'

        }
        group = {

                '$group': {
                    '_id': '$candidates_info',
                    'count': {
                        '$sum': 1
                    }
                }
            }

        add_fields = {

                '$addFields': {
                    'politicalparty': '$_id.parties',
                }
            }

        lookup_one = {

                '$lookup': {
                    'from': 'politicalparty',
                    'localField': 'parties.$id',
                    'foreignField': 'parties_id',
                    'as': 'parties_info'
                }
            }

        unwind_one = {

                '$unwind': '$parties_info'
            }

        group_one = {

                '$group': {
                    '_id': '$parties_info',
                    'votes': {
                        '$sum': '$count'
                    }
                }
            }

        add_fields_one = {

                '$addFields': {
                    'name': '$_id.name',
                    'motto': '$_id.motto',
                    '_id': '$_id._id'
                }
            }

        pipeline = [lookup, unwind, group, add_fields, lookup_one, unwind_one, group_one, add_fields_one]
        return self.query_aggregation(pipeline)

    def get_political_party_percentage_votes(self):
        position = 15
        lookup = {
            '$lookup': {
                'from': 'candidates',
                'localField': 'candidates.$id',
                'foreignField': 'parties_id',
                'as': 'candidates_info'
            }
        }
        unwind = {
            '$unwind': '$candidates_info'
        }
        group = {
            '$group': {
                '_id': '$candidates_info',
                'count': {
                    '$sum': 1
                }
            }
        }
        sort = {
            '$sort': {
                'votes': -1
            }
        }
        limit = {
            "$limit": position,
        }
        add_fields = {
            '$addFields': {
                'politicalparty': '$_id.politicalparty'
            }
        }
        lookup_one = {
            '$lookup': {
                'from': 'politicalparty',
                'localField': 'parties.$id',
                'foreignField': 'candidates_id',
                'as': 'parties_info'
            }
        }
        unwind_one = {
            '$unwind': '$parties_info'
        }
        group_one = {
            '$group': {
                '_id': '$parties_info',
                'votes': {
                    '$sum': '$count'
                }
            }
        }
        add_fields_one = {
            '$addFields': {
                'name': '$_id.name',
                'motto': '$_id.motto',
                '_id': '$_id._id'
            }
        }
        pipeline = [lookup, unwind, group, sort, limit, add_fields, lookup_one, unwind_one, group_one, add_fields_one]
        return self.query_aggregation(pipeline)
