# Builder Pattern Representation
from abc import ABC, abstractmethod


# Product class
class HttpRequest:
    def __init__(self, set_url, set_method, add_header, add_query_params, set_body):
        self.set_url = set_url
        self.set_method = set_method
        self.add_header = add_header
        self.add_query_param = add_query_params
        self.set_body = set_body

    def __str__(self):
        return f"url : {self.set_url} | method : {self.set_method} | header : {self.add_header} | query : {self.add_query_param} | body : {self.set_body}"
    

# Builder Interface    
class HttpRequestBuilder(ABC):
    @abstractmethod
    def set_url(self):
        pass


    @abstractmethod
    def set_method(self):
        pass

    @abstractmethod
    def add_header(self):
        pass


    @abstractmethod
    def add_query_param(self):
        pass


    @abstractmethod
    def set_body(self):
        pass

    @abstractmethod
    def build(self):
        pass

# Concrete Builder
class HttpConcreteBuilder(HttpRequestBuilder):
    def __init__(self):
        self.url =  None
        self.method = "GET"
        self.header = {}
        self.query_param = {}
        self.body = None

    def set_url(self, url):
        self.url = url
        return self
    

    def set_method(self, method):
        self.method = method
        return self
    
    
    def add_header(self, key, value):
        self.header[key] = value
        return self
    
    def add_query_param(self, key, value):
        self.query_param[key]=value
        return self
    
    def set_body(self, body):
        self.body = body
        return self
    
    def build(self):
        if not self.url:
            raise ValueError("URL is required")
        
        return HttpRequest(
            self.url,
            self.method,
            self.header,
            self.query_param,
            self.body
        )

# Client Code
builder = HttpConcreteBuilder()

http_request = (
    builder
    .set_url("https://api.example.com")
    .set_method("POST")
    .add_header("Authorization", "Bearer token")
    .add_header("Content-Type", "application/json")
    .add_query_param("userId", "123")
    .set_body({"name": "Tushar"})
    .build()
)

print(http_request)