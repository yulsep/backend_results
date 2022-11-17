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
