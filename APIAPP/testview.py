
# class UserView(APIView):
#     def get_object(self, pk, *arggs, **kwargs):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def get(self, pk, *args, **kwargs):
#         query = User.objects.all()
#         serializer = UserSerializer(query, many=True)

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def post(self, request, *args, **kwargs):
#         post_serializer = UserSerializer(data=request.data)
#         if post_serializer.is_valid():
#             return Response("error:", False)
#         return Response("error:", True)


# class UserDetailsView(APIView):
#     def get(self, request, pk, *args, **kwargs):
#         query_details = User.objects.get(pk=pk)
#         serializer = UserSerializer(query_details)
#         return Response(serializer.data)

#     def post(self, request, pk, *args, **kwargs):
#         receiver = User.objects.get(pk=pk)
#         dt = request.data
#         post_data = WelcomeMsgRoom.objects.create(
#             sender=request.user,
#             receiver=receiver,
#             welcome_msg=dt["welcome_msg"]
#         )
#         post_data.save()
#         post_serializer = WelcomeMsgSerializer(post_data)
#         return Response(post_serializer.data, status=status.HTTP_201_CREATED)


# class WelcomeMsgView(APIView):
#     def get_object(self, pk):
#         try:
#             return WelcomeMsgRoom.objects.get(pk=pk)
#         except WelcomeMsgRoom.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         user = CustomUser()
#         # queryset = WelcomeMsgRoom.objects.filter(sender=)
#         queryset = WelcomeMsgRoom.objects.all()
#         serializer_qry = WelcomeMsgSerializer(queryset, many=True)
#         return Response(serializer_qry.data)

#     def post(self, request, *args, **kwargs):
#         qry_data = request.data
#         data_data = WelcomeMsgRoom.objects.create(
#             sender=User(username=request.user),
#             receiver=User(username=qry_data["receiver"]),
#             welcome_msg=qry_data["welcome_msg"]
#         )
#         data_data.save()
#         post_serializer = WelcomeMsgSerializer(data_data)
#         return Response(post_serializer.data)

#     def put(self, request, pk, *args, **kwargs):
#         qry_data = self.get_object(pk)
#         serializer = WelcomeMsgSerializer(qry_data, data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk, *args, **kwargs):
#         qry_data = self.get_object(pk)
#         qry_data.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)


# class ChatRoomView(APIView):
#     def get(self, request):
#         logged_user = request.session.get('user')
#         # queryset = ChatRoom.objects.filter(user=request.user)
#         queryset = ChatRoom.objects.all()
#         serializer_qry = ChatRoomSerializer(queryset, many=True)

#         return Response(serializer_qry.data)

#     def post(self, request):
#         post_serializer = ChatRoomSerializer(data=request.data)
#         if post_serializer.is_valid():
#             post_serializer.save()
#             return Response(post_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class WelcomeMsgDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return WelcomeMsgRoom.objects.get(pk=pk)
#         except WelcomeMsgRoom.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         query_details = self.get_object(pk)
#         serializer = WelcomeMsgSerializer(query_details)
#         return Response(serializer.data)

#     def post(self, request, pk, *args, **kwargs):
#         room = self.get_object(pk)
#         qry = request.data
#         data_data = ChatRoom.objects.create(
#             message=qry["message"],
#             room=room,
#             user=request.user
#         )
#         data_data.save()

#         serializer = WelcomeMsgSerializer(data_data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
