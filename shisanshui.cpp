#include<iostream>
#include<string>
using namespace std;
class handcard
{
	public:
		char color[5];
		int num[5];
		int key;
		int rank;//代表第x墩 
		int s;//代表牌数，0则为无此牌型，若为4，且非第一墩则代表要补1张牌 
		handcard()
		{
			key=0;
			s=0;
		}
};
handcard hc[3];
class card
{
	public:
		int d,h,s,c;//花色,d红心，h黑桃，s梅花 ，c方块 
		int num;//卡牌n的数量 
		card()
		{
			d=0;
			h=0;
			s=0;
			c=0;
			num=0;
		}
};
card ca[15];
handcard  ths(int t)
{
	handcard m;
	int i,j,d=1,h=1,s=1,c=1,k=0,q=0;
	if(t==0)
	{
		return m;
	}
	for(i=10;i>=2;i--)//判断同花顺 
	{
		d=1;
		h=1;
		s=1;
		c=1;
		for(j=i;j<i+5;j++)
		{
			d*=ca[j].d;
			h*=ca[j].h;
			s*=ca[j].s;
			c*=ca[j].c;
		}
		if(d!=0)
		{
			for(j=i;j<i+5;j++)
			{
				ca[j].d--;
				ca[j].num--;
				m.s++;
				m.num[k]=j;
				m.color[k]='d';
				k++;
			}
			break;
		}
		else if(h!=0)
		{
			for(j=i;j<i+5;j++)
			{
				ca[j].h--;
				ca[j].num--;
				m.s++;
				m.num[k]=j;
				m.color[k]='h';
				k++;
			}
			break;
		}
		else if(s!=0)
		{
			for(j=i;j<i+5;j++)
			{
				ca[j].s--;
				ca[j].num--;
				m.s++;
				m.num[k]=j;
				m.color[k]='s';
				k++;
			}
			break;
		}
		else if(c!=0)
		{
			for(j=i;j<i+5;j++)
			{
				ca[j].c--;
				ca[j].num--;
				m.s++;
				m.num[k]=j;
				m.color[k]='c';
				k++;
			}
			break;
		}
	}
	if(m.s!=0)
	{
		m.key=9;//暂定 
		m.rank=t;
	}

	return m;
}
handcard  sz(int t)//顺子 
{
	handcard m;
	int i,j,n=1,k=0;
	if(t==0)
	{
		return m;
	}
	for(i=10;i>=2;i--)
	{
		n=1;
		for(j=i;j<i+5;j++)
		{
			n*=ca[j].num; 
		}
		if(n!=0)
		{
			for(j=i;j<i+5;j++)
			{
				if(ca[j].d!=0) 
				{
					ca[j].d--;
					m.color[k]='d';
				}
				else if(ca[j].h!=0)
				{
					ca[j].h--;
					m.color[k]='h';
				}
				else if(ca[j].s!=0)
				{
					ca[j].s--;
					m.color[k]='s';
				}
				else if(ca[j].c!=0)
				{
					ca[j].c--;
					m.color[k]='c';
				}
				ca[j].num--;
				m.s++;
				m.num[k]=j;
				k++;
			}
			break;
		}
	}
	if(m.s!=0)
	{
		m.key=8;//暂定 
		m.rank=t;
	}
	
	return m;
}
handcard zd(int t)//炸弹 
{
	handcard m;
	int i,j,k=0;
	if(t==0)
	{
		return m;
	}
	for(i=14;i>=1;i--)
	{
		if(ca[i].num==4)
		{
			for(j=0;j<4;j++)
			{
				m.num[k]=i;
				k++;
			}
			ca[i].num-=4;
			m.s+=4;
			ca[i].d--;
			ca[i].h--;
			ca[i].s--;
			ca[i].c--;
			m.color[0]='d';
			m.color[1]='h';
			m.color[2]='d';
			m.color[3]='c';
			break;
		}
	}
	if(m.s!=0)
	{
		m.key=8;//暂定 
		m.rank=t;
	}
	return m;
} 
handcard hl(int t)//葫芦 
{
	handcard m;
	int i,j,q=0,k=0;
	if(t==0)
	{
		return m;
	}
	for(i=14;i>=1;i--)
	{
		if(ca[i].num>=3)
		{
			for(j=2;j<=i-1;j++)
			{
				if(ca[j].num>=2)
				{
					for(k=0;k<2;k++)
					{
						if(ca[j].d!=0) 
						{
							ca[j].d--;
							m.color[k]='d';
						}
						else if(ca[j].h!=0)
						{
							ca[j].h--;
							m.color[k]='h';
						}
						else if(ca[j].s!=0)
						{
							ca[j].s--;
							m.color[k]='s';
						}
						else if(ca[j].c!=0)
						{
							ca[j].c--;
							m.color[k]='c';
						}
						ca[j].num--;
						m.s++;
						m.num[k]=j;
					}
					for(k=2;k<5;k++)
					{
						if(ca[i].d!=0) 
						{
							ca[i].d--;
							m.color[k]='d';
						}
						else if(ca[i].h!=0)
						{
							ca[i].h--;
							m.color[k]='h';
						}
						else if(ca[i].s!=0)
						{
							ca[i].s--;
							m.color[k]='s';
						}
						else if(ca[i].c!=0)
						{
							ca[i].c--;
							m.color[k]='c';
						}
						ca[i].num--;
						m.s++;
						m.num[k]=i;
					}
					q=1;
					break;
				}
				
			} 
		}
		if(q==1) 
		{
			break;
		}
	}
	if(m.s!=0)
	{
		m.key=7;//暂定 
		m.rank=t;
	}
	return m;
}
handcard th(int t)//同花
{
	handcard m;
	int i,j,d=0,h=0,s=0,c=0,k=0,key=0,f=0;
	if(t==0)
	{
		return m;
	}
	for(i=2;i<=14;i++)
	{
		d+=ca[i].d;
		h+=ca[i].h;
		s+=ca[i].s;
		c+=ca[i].c;
	}
	i=0;
	if(d>=5)
	{
		for(i=14;i>=2;i--)
		{
			if(ca[i].d==1)
			{
				break;
			}
		}
		if(i>key)
		{
			key=i;
			f=1;
		}
	}
	i=0;
	if(s>=5)
	{
		for(i=14;i>=2;i--)
		{
			if(ca[i].s==1)
			{
				break;
			}
		}
		if(i>key)
		{
			key=i;
			f=2;
		}
	}
	i=0;
	if(h>=5)
	{
		for(i=14;i>=2;i--)
		{
			if(ca[i].h==1)
			{
				break;
			}
		}
		if(i>key)
		{
			key=i;
			f=3;
		}
	}
	i=0;
	if(c>=5)
	{
		for(i=14;i>=2;i--)
		{
			if(ca[i].c==1)
			{
				break;
			}
		}
		if(i>key)
		{
			key=i;
			f=4;
		}
	}
	for(i=key;i>=2;i--)
	{
		if(k==5)
		{
			break;
		}
		if(f==1)
		{
			if(ca[i].d==1)
			{
				ca[i].d--;
				ca[i].num--;
				m.s++;
				m.num[k]=i;
				m.color[k]='d';
				k++;
			}
		}
		else if(f==2)
		{
			if(ca[i].s==1)
			{
				ca[i].s--;
				ca[i].num--;
				m.s++;
				m.num[k]=i;
				m.color[k]='s';
				k++;
			}
		}
		else if(f==3)
		{
			if(ca[i].h==1)
			{
				ca[i].h--;
				ca[i].num--;
				m.s++;
				m.num[k]=i;
				m.color[k]='h';
				k++;
			}
		}
		else if(f==4)
		{
			if(ca[i].c==1)
			{
				ca[i].c--;
				ca[i].num--;
				m.s++;
				m.num[k]=i;
				m.color[k]='c';
				k++;
			}
		}
	}
	if(m.s!=0)
	{
		m.key=6;//暂定 
		m.rank=t;
	}
	
	return m;
}
handcard st(int t)//三条
{
	handcard m;
	int i,j,k=0;
	for(i=14;i>=2;i--) 
	{
		if(ca[i].num==3)
		{
			for(j=0;j<3;j++)
			{
				if(ca[i].d==1)
				{
					ca[i].d--;
					ca[i].num--;
					m.s++;
					m.num[k]=i;
					m.color[k]='d';
					k++;
				}
				else if(ca[i].h==1)
				{
					ca[i].h--;
					ca[i].num--;
					m.s++;
					m.num[k]=i;
					m.color[k]='h';
					k++;
				}
				else if(ca[i].s==1)
				{
					ca[i].s--;
					ca[i].num--;
					m.s++;
					m.num[k]=i;
					m.color[k]='s';
					k++;
				}
				else if(ca[i].c==1)
				{
					ca[i].c--;
					ca[i].num--;
					m.s++;
					m.num[k]=i;
					m.color[k]='c';
					k++;
				}
			}
			
		}
	}
	if(m.s!=0)
	{
		m.key=6;//暂定 
		m.rank=t;
	}
	return m;
} 
handcard ed(int t)
{
	handcard m;
	int i,j,q=0,k=0;
	if(t==0)
	{
		return m;
	}
	for(i=14;i>=1;i--)
	{
		if(ca[i].num==2)
		{
			for(j=i-1;j>=1;j--)
			{
				if(ca[j].num>=2)
				{
					for(k=0;k<2;k++)
					{
						if(ca[j].d!=0) 
						{
							ca[j].d--;
							m.color[k]='d';
						}
						else if(ca[j].h!=0)
						{
							ca[j].h--;
							m.color[k]='h';
						}
						else if(ca[j].s!=0)
						{
							ca[j].s--;
							m.color[k]='s';
						}
						else if(ca[j].c!=0)
						{
							ca[j].c--;
							m.color[k]='c';
						}
						ca[j].num--;
						m.s++;
						m.num[k]=j;
					}
					for(k=2;k<4;k++)
					{
						if(ca[i].d!=0) 
						{
							ca[i].d--;
							m.color[k]='d';
						}
						else if(ca[i].h!=0)
						{
							ca[i].h--;
							m.color[k]='h';
						}
						else if(ca[i].s!=0)
						{
							ca[i].s--;
							m.color[k]='s';
						}
						else if(ca[i].c!=0)
						{
							ca[i].c--;
							m.color[k]='c';
						}
						ca[i].num--;
						m.s++;
						m.num[k]=i;
					}
					q=1;
					break;
				}
				
			} 
		}
		if(q==1) 
		{
			break;
		}
	}
	if(m.s!=0)
	{
		m.key=6;//暂定 
		m.rank=t;
	}
	return m;
}
handcard dz(int t)
{
	handcard m;
	int i,j,q=0,k=0;
	for(i=14;i>=2;i--)
	{
		if(ca[i].num==2)
		{
			for(k=0;k<2;k++)
			{
				if(ca[i].d!=0) 
				{
					ca[i].d--;
					m.color[k]='d';
				}
				else if(ca[i].h!=0)
				{
					ca[i].h--;
					m.color[k]='h';
				}
				else if(ca[i].s!=0)
				{
					ca[i].s--;
					m.color[k]='s';
				}
				else if(ca[i].c!=0)
				{
					ca[i].c--;
					m.color[k]='c';
				}
				ca[i].num--;
				m.s++;
				m.num[k]=i;
				q=1;
			}
			if(q==1)
			{
				break;
			}
		}
	}
	if(m.s!=0)
	{
		m.key=6;//暂定 
		m.rank=t;
	}	
	return m;
}
int main()
{
	char fc,nu;
	string s;
	int num,i,n=0,j,m,t;
	for(i=0;i<13;i++)
	{
		cin>>s;
		if(s[1]=='J')
		{
			n=11;
		}
		else if(s[1]=='Q')
		{
			n=12;
		}
		else if(s[1]=='K')
		{
			n=13; 
		}
		else if(s[1]=='A')
		{
			n=14;
		}
		else
		{
			n=(int)s[1]-48;
		}
		if(s.length()==3)
		{
			n=10;
		}
		if(s[0]=='&')//红心 
		{
			ca[n].d++;
			ca[n].num++;
		}
		else if(s[0]=='$')//黑桃 
		{
			ca[n].h++;
			ca[n].num++;
		}
		else if(s[0]=='#')//方块
		{
			ca[n].c++;
			ca[n].num++;
		}
		else if(s[0]=='*')//梅花
		{
			ca[n].s++;
			ca[n].num++;
		}
	}
	for(i=2;i>=0;i--)
	{
		hc[i]=ths(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		hc[i]=zd(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		hc[i]=hl(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		hc[i]=th(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		hc[i]=sz(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		hc[i]=st(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		hc[i]=ed(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		hc[i]=dz(i);
		if(hc[i].s!=0)
		{
			continue;
		}
		for(j=14;j>=2;j--)
		{
			if(ca[j].num!=0)
			{
				ca[j].num--;
				if(ca[j].d!=0)
				{
					ca[j].d--;
					hc[i].color[0]='d';
				}
				else if(ca[j].s!=0)
				{
					ca[j].s--;
					hc[i].color[0]='s';
				}
				else if(ca[j].h!=0)
				{
					ca[j].h--;
					hc[i].color[0]='h';
				}
				else if(ca[j].c!=0)
				{
					ca[j].c--;
					hc[i].color[0]='c';
				}
				hc[i].num[0]=j;
				hc[i].s++;
				break;
			} 
		}
	}
	for(i=2;i>=0;i--)
	{
		if(i!=0)
		{
			m=5;
		}
		else
		{
			m=3;
		}
		while(hc[i].s<m)
		{
			t=hc[i].s;
			for(j=2;j<=14;j++)
			{
				if(ca[j].num!=0)
				{
					ca[j].num--;
					if(ca[j].d!=0)
					{
						ca[j].d--;
						hc[i].color[t]='d';
					}
					else if(ca[j].s!=0)
					{
						ca[j].s--;
						hc[i].color[t]='s';
					}
					else if(ca[j].h!=0)
					{
						ca[j].h--;
						hc[i].color[t]='h';
					}
					else if(ca[j].c!=0)
					{
						ca[j].c--;
						hc[i].color[t]='c';
					}
					hc[i].num[t]=j;
					hc[i].s++;
					break;
				} 
			}
		}
	}
	for(i=0;i<3;i++)
	{
		t=hc[i].s;
		for(j=0;j<t;j++)
		{
			if(j!=t-1)
			{
				nu=' ';
			}
			else 
			{
				nu='\n';
			}
			if(hc[i].color[j]=='d')
			{
				hc[i].color[j]='&';
			}
			else if(hc[i].color[j]=='h')
			{
				hc[i].color[j]='$';
			}
			else if(hc[i].color[j]=='c')
			{
				hc[i].color[j]='#';
			}
			else if(hc[i].color[j]=='s')
			{
				hc[i].color[j]='*';
			}
			if(hc[i].num[j]==11)
			{
				cout<<hc[i].color[j]<<'J'<<nu;
			}
			else if(hc[i].num[j]==12)
			{
				cout<<hc[i].color[j]<<'Q'<<nu;
			}
			else if(hc[i].num[j]==13)
			{
				cout<<hc[i].color[j]<<'K'<<nu;
			}
			else if(hc[i].num[j]==14)
			{
				cout<<hc[i].color[j]<<'A'<<nu;
			}
			else
			{
				cout<<hc[i].color[j]<<hc[i].num[j]<<nu;
			}	
		}
	}
	system("pause"); 
	return 0; 
}
