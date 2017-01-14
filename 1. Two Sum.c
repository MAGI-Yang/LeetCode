/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
	int j,i=NULL;
	int * result = malloc(sizeof(int) * 2);
	for(i=0; i<numsSize-1; i++)
	{
		for(j=i+1; j<numsSize; j++)
		{
			if( target == (nums[i]+nums[j]) )
			{
				result[0]=i;
				result[1]=j;
				return result;
			}
		}
	}
}

