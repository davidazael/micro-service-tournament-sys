

init:
	${MAKE} -C ./users_crud
	${MAKE} -C ./tournaments_crud
	${MAKE} -C ./association_tourneys_users

clean:
	${MAKE} -C ./users_crud clean
	${MAKE} -C ./tournaments_crud clean
	${MAKE} -C ./association_tourneys_users clean

dcu:
	docker-compose up --build --remove-orphans

dcd:
	docker-compose down
