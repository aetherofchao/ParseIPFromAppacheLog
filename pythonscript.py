
def main():

	file = open("access.log","r")
	lines = file.readlines()
	file.close()

	Ips = {}

	for line in lines:
		ip,method = getIP(line)
		if ip in Ips:
			Ips[ip]["0total"] +=1
			if (method in Ips[ip]):
				Ips[ip][method] +=1
			else:
				Ips[ip][method] = 1
			
		else:
			Ips[ip] = {"0total": 1, "GET":0, "HEAD":0, "POST":0, "PUT":0, "DELETE":0, "TRACE":0, "OPTIONS":0, "CONNECT":0, "PATCH":0 }
			if (method in Ips[ip]):
				Ips[ip][method] +=1
			else:
				Ips[ip][method] = 1

	file = open("output.csv","w+")

	for i in Ips:
		ip = Ips[i]
		file.write(i + ",")
		for method in sorted(ip):
			n = str(Ips[i][method])
			if (n != "0"):
				file.write(method +":"+n+",")
		file.write("\n")

	file.close()


def getIP(line):
	ip = ""
	method= ""
	for i in range(100):
		if (line[i] == " "): break
		ip += line[i]
	for i in range(100):
		if (line[i-1] == '"'):
			for j in range(100):
				if (line[i+j]== " "): break
				method += line[i+j]
			break
	return [ip,method]


if __name__ == '__main__':
	main()