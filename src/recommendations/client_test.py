import grpc
from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

request = RecommendationRequest(
    user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
    )
print(request.category)

# request = RecommendationRequest(
#     user_id="oops", category=BookCategory.SCIENCE_FICTION, max_results=3
#     )

request = RecommendationRequest(
    user_id=1, category=BookCategory.SCIENCE_FICTION
    )
print(request.max_results)

channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)
request = RecommendationRequest(
    user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
    )
#client.Recommend(request)

