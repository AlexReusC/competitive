#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, n, tmp;
	cin >> t;
	while (t--)
	{
		cin >> n;
		vector<int> a;
		map<int, int> occurrences;
		for (int i = 0; i < n; i++)
		{
			cin >> tmp;
			if (occurrences.find(tmp) == occurrences.end())
			{
				occurrences[tmp] = 1;
			}
			else
			{
				occurrences[tmp]++;
			}
			a.push_back(tmp);
		}

		int sets = 0;
		for (auto i = occurrences.begin(); i != occurrences.end(); i++)
		{
			while (occurrences[i->first] > 0)
			{
				sets++;
				occurrences[i->first]--;
				int increment = 1;
				while (occurrences.find(i->first + increment) != occurrences.end() && occurrences[i->first + increment] != 0)
				{
					occurrences[i->first + increment]--;
					increment++;
				}
			}
		}

		cout << sets << endl;
	}

	return 0;
}