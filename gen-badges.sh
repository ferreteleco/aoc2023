poetry run pytest tests --doctest-modules --junit-xml=reports/junit/junit-test-report.xml --cov=aoc2023 --cov-report=xml --cov-report=lcov

poetry run flake8 aoc2023 --exit-zero --statistics --tee --output-file reports/flake8/flake8stats.txt

genbadge tests -i reports/junit/junit-test-report.xml -o reports/badges/junit-tests-badge.svg
genbadge flake8 -i reports/flake8/flake8stats.txt -o reports/badges/flake8-badge.svg
genbadge coverage -i reports/coverage/cov.xml -o reports/badges/cov-badge.svg
