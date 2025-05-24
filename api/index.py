from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your original list of students
students_list = [
  {
    "name": "vA",
    "marks": 75
  },
  {
    "name": "caY2",
    "marks": 65
  },
  {
    "name": "EFQB5Hizwz",
    "marks": 96
  },
  {
    "name": "a",
    "marks": 31
  },
  {
    "name": "mhdr",
    "marks": 36
  },
  {
    "name": "hf7Z1M",
    "marks": 46
  },
  {
    "name": "YmYUuI",
    "marks": 12
  },
  {
    "name": "gSQMeKtcSf",
    "marks": 24
  },
  {
    "name": "GsfL9Rtfi",
    "marks": 21
  },
  {
    "name": "9TbH7xT",
    "marks": 57
  },
  {
    "name": "iQKv",
    "marks": 40
  },
  {
    "name": "C482",
    "marks": 25
  },
  {
    "name": "cBByvNx",
    "marks": 6
  },
  {
    "name": "UD3rW",
    "marks": 69
  },
  {
    "name": "Rz",
    "marks": 65
  },
  {
    "name": "pHOxv4A",
    "marks": 0
  },
  {
    "name": "2qoGu",
    "marks": 63
  },
  {
    "name": "u5Ytpf",
    "marks": 81
  },
  {
    "name": "z3",
    "marks": 80
  },
  {
    "name": "IMO4IpM",
    "marks": 67
  },
  {
    "name": "gA6tAKWv",
    "marks": 19
  },
  {
    "name": "9o3kvdO",
    "marks": 12
  },
  {
    "name": "3Yp9TYP",
    "marks": 72
  },
  {
    "name": "t7VWWY41sE",
    "marks": 58
  },
  {
    "name": "dPn7TE",
    "marks": 53
  },
  {
    "name": "nfHpklW",
    "marks": 59
  },
  {
    "name": "GDIex",
    "marks": 48
  },
  {
    "name": "k",
    "marks": 67
  },
  {
    "name": "TNsb",
    "marks": 72
  },
  {
    "name": "7NIvziW5sx",
    "marks": 71
  },
  {
    "name": "orqN8JS",
    "marks": 61
  },
  {
    "name": "V7",
    "marks": 44
  },
  {
    "name": "m",
    "marks": 80
  },
  {
    "name": "71J6ORc6z3",
    "marks": 61
  },
  {
    "name": "59neh",
    "marks": 66
  },
  {
    "name": "36gJpPt",
    "marks": 4
  },
  {
    "name": "GLl58Sviv",
    "marks": 53
  },
  {
    "name": "RONLyW0za",
    "marks": 19
  },
  {
    "name": "XO",
    "marks": 65
  },
  {
    "name": "IQt",
    "marks": 88
  },
  {
    "name": "zKjtckityE",
    "marks": 57
  },
  {
    "name": "fpR4pzY8g",
    "marks": 1
  },
  {
    "name": "n7uOA60O4e",
    "marks": 34
  },
  {
    "name": "tnawSC",
    "marks": 70
  },
  {
    "name": "sVVdjYGn",
    "marks": 83
  },
  {
    "name": "czM",
    "marks": 69
  },
  {
    "name": "y0s1Emk",
    "marks": 83
  },
  {
    "name": "Hq",
    "marks": 33
  },
  {
    "name": "pOj0uDlX",
    "marks": 82
  },
  {
    "name": "n8J",
    "marks": 43
  },
  {
    "name": "1EQoWakF",
    "marks": 73
  },
  {
    "name": "vCJ1IhK",
    "marks": 67
  },
  {
    "name": "RKjPC1",
    "marks": 77
  },
  {
    "name": "q",
    "marks": 97
  },
  {
    "name": "PgBh",
    "marks": 13
  },
  {
    "name": "hqh0",
    "marks": 59
  },
  {
    "name": "SCVT",
    "marks": 1
  },
  {
    "name": "2V7aC2",
    "marks": 72
  },
  {
    "name": "DhjXX0c",
    "marks": 29
  },
  {
    "name": "nEbiOG",
    "marks": 51
  },
  {
    "name": "1mo28tw0",
    "marks": 71
  },
  {
    "name": "HsQgay",
    "marks": 60
  },
  {
    "name": "Eo0wfEFhK",
    "marks": 46
  },
  {
    "name": "v2eqn",
    "marks": 6
  },
  {
    "name": "Vs",
    "marks": 88
  },
  {
    "name": "eOCUCKg0gj",
    "marks": 33
  },
  {
    "name": "rf8a",
    "marks": 85
  },
  {
    "name": "GfzUdCLp",
    "marks": 32
  },
  {
    "name": "y3GEO",
    "marks": 86
  },
  {
    "name": "HuToqik",
    "marks": 37
  },
  {
    "name": "EmExNy",
    "marks": 99
  },
  {
    "name": "ZoaAtJ",
    "marks": 58
  },
  {
    "name": "5DHofoZI",
    "marks": 45
  },
  {
    "name": "SxNgNl",
    "marks": 96
  },
  {
    "name": "9dLOU",
    "marks": 97
  },
  {
    "name": "F9",
    "marks": 95
  },
  {
    "name": "CQ21WAGt",
    "marks": 53
  },
  {
    "name": "UL",
    "marks": 16
  },
  {
    "name": "OSYiho70X",
    "marks": 49
  },
  {
    "name": "hVQV40",
    "marks": 63
  },
  {
    "name": "epRrGgB",
    "marks": 95
  },
  {
    "name": "kD",
    "marks": 85
  },
  {
    "name": "w84z2C",
    "marks": 49
  },
  {
    "name": "fGY2",
    "marks": 59
  },
  {
    "name": "tp",
    "marks": 40
  },
  {
    "name": "1",
    "marks": 6
  },
  {
    "name": "Lsc",
    "marks": 24
  },
  {
    "name": "FFieTZ",
    "marks": 96
  },
  {
    "name": "Vj8Tu",
    "marks": 65
  },
  {
    "name": "xnNpLXz",
    "marks": 18
  },
  {
    "name": "PbN3BQj2",
    "marks": 51
  },
  {
    "name": "XK5wTMg9",
    "marks": 17
  },
  {
    "name": "WmSTkkmyPa",
    "marks": 68
  },
  {
    "name": "RAJlRDgT",
    "marks": 57
  },
  {
    "name": "5p",
    "marks": 64
  },
  {
    "name": "uKj",
    "marks": 37
  },
  {
    "name": "DS4K",
    "marks": 56
  },
  {
    "name": "30566",
    "marks": 71
  },
  {
    "name": "M4",
    "marks": 26
  },
  {
    "name": "E6",
    "marks": 9
  }
]
# Convert list to dictionary for fast lookup
students = {student["name"]: student["marks"] for student in students_list}

@app.route('/', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, 0) for name in names]
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run()
