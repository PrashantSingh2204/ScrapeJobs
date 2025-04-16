from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape_jobs', methods=['GET'])
def scrape_jobs():
    # Get query parameters for keywords and location
    keywords = request.args.get('keywords', 'software engineer')
    location = request.args.get('location', 'San Francisco, CA')
    url = f"https://www.linkedin.com/jobs/search/?currentJobId=4205451182&keywords=java&location=india"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        soup = BeautifulSoup(response.text, 'html.parser')
        
        jobs = []
        for job in soup.find_all('div', class_='result-card__contents'):
            title = job.find('h3', class_='result-card__title').text.strip()
            company = job.find('h4', class_='result-card__subtitle').text.strip()
            location = job.find('span', class_='job-result-card__location').text.strip()
            link = job.find('a', class_='result-card__full-card-link')['href']
            jobs.append({'title': title, 'company': company, 'location': location, 'link': link})
        
        return jsonify(jobs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)