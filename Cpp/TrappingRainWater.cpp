    int ans=0,res[30002]={};

    void solve(int p,vector<int>& height) {
        if(p>=height.size()-1)
            return;
        while(p<height.size() && height[p]==0)
            p++;
        int q=p+1;
        int m=-1,j;
        while(q<height.size() && height[q]<height[p])
        {
            if(height[q]>=m)
            {
                j=q;
                m=height[q];
            }
            q++;
        }
        if(q<height.size())
        {
            ans+=height[p]*(q-p-1)-(res[q]-res[p+1]);
            solve(q,height);
        }
        else
        {
            ans+=height[j]*(j-p-1)-(res[j]-res[p+1]);
            solve(j,height);
        }
    }

    int trap(vector<int>& height) {
        if(height.size()==0)
            return 0;
        res[0]=0;
        for(int i=0;i<height.size();i++)
        {
            res[i+1]+=res[i];
            res[i+1]+=height[i];
        }
        solve(0,height);
        return ans;
    }
