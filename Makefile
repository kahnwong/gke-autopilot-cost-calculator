setup:
	pyenv virtualenv 3.11.4 gke-autopilot-cost-calculator
	pyenv local gke-autopilot-cost-calculator
	pip install -r requirements.txt
	# pip install -r requirements-dev.txt
	pip install -e .
