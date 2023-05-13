start:
	@echo "==============================================="
	@echo "Make: starting algorithm-2 container"
	@echo "==============================================="
	@docker compose run -p 8000:8000 --rm dev

stop:
	@echo "==============================================="
	@echo "Make: stopping algorithm-2 container"
	@echo "==============================================="
	@docker stop $$(docker ps -qf "name=algorithm-2") > /dev/null