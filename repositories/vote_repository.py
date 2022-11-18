from bson import ObjectId

from models.vote import Vote
from repositories.interface_repository import InterfaceRepository


class VoteRepository(InterfaceRepository[Vote]):
    def get_table_in_candidate(self, candidate_id: str) -> list:
        """

        :param candidate_id:
        :return:
        """
        query = {"candidate.$id": ObjectId(candidate_id)}
        return self.query(query)


