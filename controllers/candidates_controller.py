from models.candidates import Candidates
from repositories.candidates_repository import CandidatesRepository


class CandidateController:
    #constructor
    def __init__(self):
        print("Candidate controller ready")
        self.candidates_repository = CandidatesRepository()

    def index(self) -> list:
        """
        This method get a candidate list
        :return:
        """
        print("Get all")
        return self.candidates_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        this method obtains a candidate indicating its id parameter
        :param id_:
        :return:
        """
        print("Show by id")
        return self.candidates_repository.fin_by_id(id_)

    def create(self, candidate_: dict) -> dict:
        """
        This method allows you to create and attach a candidate
        :param candidate_:
        :return:
        """
        print("Insert")
        candidates = Candidates(candidate_)
        return self.candidates_repository.save(candidates)

    def update(self, id_: str, candidate_: dict) -> dict:
        """
        This method allows you to update the data of a candidate
        :param id_:
        :param candidate_:
        :return:
        """
        print("Update")
        candidate = Candidates(candidate_)
        return self.candidates_repository.update(id_, candidate)

    def delete(self, id_: str) -> str:
        """
        this method allows to eliminate a candidate
        :param id_:
        :return:
        """
        print("Delete" + id_)
        return self.candidates_repository.delete(id_)
