from models.candidates import Candidates
from models.political_party import PoliticalParty
from repositories.candidates_repository import CandidatesRepository
from repositories.political_party_repository import PoliticalPartyRepository

class CandidateController:
    # constructor
    def __init__(self):
        print("Candidate controller ready")
        self.candidates_repository = CandidatesRepository()
        self.candidates_repository = PoliticalPartyRepository()

    def index(self) -> list:
        """
        This method get a candidate list
        :return:
        """
        return self.candidates_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        this method obtains a candidate indicating its id parameter
        :param id_:
        :return:
        """
        return self.candidates_repository.find_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """
        This method allows you to create and attach a candidate
        :param candidate_:
        :return:
        """
        candidates = Candidates(candidate_)
        return self.candidates_repository.save(candidates)

    def update(self, id_: str, candidate_: dict) -> dict:
        """
        This method allows you to update the data of a candidate
        :param id_:
        :param candidate_:
        :return:
        """
        candidate = Candidates(candidate_)
        return self.candidates_repository.update(id_, candidate)

    def delete(self, id_: str) -> str:
        """
        this method allows to eliminate a candidate
        :param id_:
        :return:
        """
        return self.candidates_repository.delete(id_)

    """
        Political party and candidate relationship
    """
    def political_party_assign(self, candidate_id: str, political_party_id: str) -> dict:
        candidate_dict = self.candidates_repository.find_by_id(candidate_id)
        candidate_obj = PoliticalParty(candidate_dict)
        political_party_dict = self.candidates_repository.find_by_id(political_party_id)
        political_party_obj = PoliticalParty(political_party_dict)
        candidate_obj.parties = political_party_obj
        return self.candidates_repository.save(candidate_obj)

