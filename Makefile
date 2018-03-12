PROG=smart-reminder
VUE_PATH=$(PROG)/templates

build: build-vue build-python-dependencies
	@echo "Congratulations! You've built your smart-reminder."
	@echo "To run it, simply execute 'make run'"

build-python-dependencies:
	pip3 install -r requirements.txt

build-vue: build-vue-dependencies
	cd $(VUE_PATH) && npm run build

build-vue-dependencies:
	cd $(VUE_PATH) && npm install --save-dev

run: 
	cd $(PROG) && ./run.sh
