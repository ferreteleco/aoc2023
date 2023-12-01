poetry run pytest tests --doctest-modules --junit-xml=reports/junit/junit-test-report.xml --cov=aoc2023 --cov-report=xml --cov-report=lcov

rm reports/flake8/flake8stats.txt
poetry run flake8 aoc2023 --exit-zero --statistics --tee --output-file reports/flake8/flake8stats.txt

poetry run genbadge tests -i reports/junit/junit-test-report.xml -o reports/badges/junit-tests-badge.svg
poetry run genbadge flake8 -i reports/flake8/flake8stats.txt -o reports/badges/flake8-badge.svg
poetry run genbadge coverage -i reports/coverage/cov.xml -o reports/badges/cov-badge.svg
