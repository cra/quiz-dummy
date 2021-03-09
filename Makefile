NAMESPACE = shrimpsizemoose
REPOSITORY = quiz-dummy
TAG ?= latest

FULL_TAG ?= ${NAMESPACE}/${REPOSITORY}:${TAG}

@build:
	docker build . -t ${FULL_TAG}

@run:
	docker run -it --rm -p 8000:8000 ${FULL_TAG} --name dummy-quiz-server

@push:
	docker push ${FULL_TAG}
