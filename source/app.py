from flask import Flask
app = Flask(__name__)

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-e')
parser.add_argument('--host')
args = parser.parse_args()

env, hostPort = args.e, args.host
app.config['env'], app.config['host'] = env, hostPort

print('Current environment : ', app.config['env'], ' Interface: ', app.config['host'].partition(":")[0], ' Port: ', app.config['host'].partition(":")[2])

@app.route("/")
def create_app():
    return "Current environment is >>> " + app.config['env'] + " <<< listening on [" + app.config['host'] + "]"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=app.config['host'].partition(":")[2])
