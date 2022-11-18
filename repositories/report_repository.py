from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class ReportRepository(InterfaceRepository[Vote]):
    def get_votes_by_candidate(self) -> list:
        query_aggregation = {
            "$group": {
                "_id": "$candidate",
                "votes_by_candidate": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query_aggregation]
        return self.query_aggregation(pipeline)

    def get_votes_by_table(self):
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

    def get_votes_for_political_party(self):
        pass