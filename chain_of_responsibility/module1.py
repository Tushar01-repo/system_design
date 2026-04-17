from abc import ABC, abstractmethod

# abstract handler
class SupportHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def approval_status(self, request):
        pass


# concrete class
class TeamLeadApproval(SupportHandler):
    def approval_status(self, request):
        if request <= 10000:
            print(f"Team Lead can approve this request as {request} <= 10000")

        elif self.next_handler:
            self.next_handler.approval_status(request)


class ManagerApproval(SupportHandler):
    def approval_status(self, request):
        if ((request>10000) and (request<=50000)):
            print(f"Manager can approve this request as it is 10000 < {request} <= 50000")

        elif self.next_handler:
            self.next_handler.approval_status(request)


class DirectorApproval(SupportHandler):
    def approval_status(self, request):
        if ((request > 50000) and (request < 100000)):
            print(f"Director approved this request as {request} > 50000")

        else:
            print("Sorry your approval request can't be approved as it is exceeding the limit")



# setup chain
handler_chain = TeamLeadApproval(
    ManagerApproval(
        DirectorApproval()
    )
)


# client code 
if __name__ == "__main__":
    
    amount = [5000, 17000, 58000, 150000]

    for i in amount:
        handler_chain.approval_status(i)