get_bin = lambda x, n: format(x, 'b').zfill(n) ####     get_bin(2,32) -> 0000..0010 (30x0s + 10)



##############		FUNCTION DID IN EACH STEP		#################

def Ch(x,y,z):
	a=(x&y)^(~x&z)
	return a	
	
def Maj(x,y,z):
	a=(x&y)^(x&z)^(y&z)
	return a

def f1(x):
	a=get_bin(x,32)
	i=rr(a,2)
	j=rr(a,13)
	k=rr(a,22)
	
	i=int(i,2)
	j=int(j,2)
	k=int(k,2)
	
	return i^j^k

def f2(x):
	a=get_bin(x,32)
	i=rr(a,6)
	j=rr(a,11)
	k=rr(a,25)
	
	i=int(i,2)
	j=int(j,2)
	k=int(k,2)
	
	return i^j^k
def f3(x):
	a=get_bin(x,32)
	i=rr(a,7)
	j=rr(a,18)
	k=x>>3
	
	i=int(i,2)
	j=int(j,2)

	
	return i^j^k
def f4(x):
	a=get_bin(x,32)
	i=rr(a,17)
	j=rr(a,19)
	k=x>>10
	
	i=int(i,2)
	j=int(j,2)

	return i^j^k
	
	
################################################################################	
def rr (x,y):
	a= (x[-y:] + x[:-y]) 	
	return a

#####################################################################################
##################CONVERT STRING TO WORD LIST 'w'###################################


mod=4294967296  ####     2^32
w=[]
s='Group 14'     ################# Message
print "\n"+s
slen=len(s)
i=0
a= [ord(c) for c in s] ##### convert message to respective ASCII
i=0

k=[1116352408,3624381080,3835390401,2554220882,666307205,2730485921,430227734,1955562222,1899447441,310598401,4022224774,2821834349,773529912,2820302411,506948616,2024104815,3049323471,607225278,264347078,2952996808,1294757372,3259730800,659060556,2227730452,3921009573,1426881987,604807628,2952996808,1396182291,3345764771,883997877,2361852424,961987163,1925078388,770255983,3336571891,1695183700,3516065817,958139571,2428436474,1508970993,2162078206,1249150122,3584528711,1986661051,3600352804,1322822218,2756734187,2453635748,2614888103,1555081692,113926993,2177026350,4094571909,1537002063,3204031479,2870763221,3248222580,1996064986,338241895,2456956037,275423344,1747873779,3329325298]

h1=1779033703
h2=3144134277
h3=1013904242
h4=2773480762

h5=1359893119
h6=2600822924
h7=528734635
h8=1541459225


############## FILL UPTO 512 BITS IN a
a.append(128) # 10000000
n=len(s)
if(n%448!=0):
	for i in range(n,55):
		a.append(0)
########## STORE LENGTH IN LAST 64 BITS	
n=len(s)
slenbin=get_bin(n,64)
i=0
j=8
while j<=64:
	q=slenbin[i:j]
	a.append(int(q,2))
	i=i+8
	j=j+8

#print len(a)
#print a
		
#for i in a:
#	print get_bin(i,8)
i=0
n=len(a)
j=0


################ CREATE 32 BIT WORDS IN w
while i<n:
	temp=get_bin(a[i],8)+get_bin(a[i+1],8)+get_bin(a[i+2],8)+get_bin(a[i+3],8)
	w.append(int(temp,2))
	i=i+4
	
#print w

#################################################################################
for i in range(16,64):
	w.append(  (f4(w[i-2])+w[i-7]+f1(w[i-15])+w[i-16])%mod  )

#print w
############################################ ROUND  (64 TIMES)
for i in range(64):
	temp1=(h8+f2(h5)+Ch(h5,h6,h7)+k[i]+w[i])%mod
	temp2=(f1(h1)+Maj(h1,h2,h3))%mod
	t8=h7
	t7=h6
	t6=h5
	t5=(h4+temp1)%mod
	t4=h3
	t3=h2
	t2=h1
	t1=(temp1+temp2)%mod
	
	h1=(t1+h1)%mod
	h2=(t2+h2)%mod
	h3=(t3+h3)%mod
	h4=(t4+h4)%mod
	h5=(t5+h5)%mod
	h6=(t6+h6)%mod
	h7=(t7+h7)%mod
	h8=(t8+h8)%mod


print hex(h1)[2:]+" "+hex(h2)[2:]+" "+hex(h3)[2:]+" "+hex(h4)[2:]+" "+hex(h5)[2:]+" "+hex(h6)[2:]+" "+hex(h7)[2:]+" "+hex(h8)[2:]

### 0x123bc456 -> 123bc456

















