
# coding: utf-8

# In[7]:


def bytes_from_file(filename, chunksize=2068):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

# example:

bin_output = []

for b in bytes_from_file('./telemetry.bin'):
    bin_output.append(b)


# In[10]:


print (bin_output[112:136])


# In[11]:


print (bin_output[136:160])


# In[12]:


print (bin_output[65:90])


# In[1]:


import pandas as pd


# Time is in Package - 65-87
# 
# Velocity is in Mnemonic - 136 - 156
# 
# Position is in Mnemonic - 112 - 132

# In[2]:


df = pd.read_csv('./TLM_LIST.csv')

df.head()


# In[21]:


# extract byte column from Package where value is TIME

time_pos = list(df[df['Package']=='TIME']['Byte'])

time_pos


# In[22]:


# getting data for the time 

time_data = []


for x in time_pos:
    time_data.append(bin_output[int(x)])


print (time_data)


# In[24]:


vel_pos = [136,140,144,148,152,156]

vel_pos


# In[25]:


vel_data = []

for x in vel_pos:
    vel_data.append(bin_output[int(x)])


print (vel_data)


# In[ ]:


position = [112, 116, 120, 124, 128, 132]


pos_data = []

for x in position:
    pos_data.append(bin_output[int(x)])


print (pos_data)


# ## Read the new file

# In[2]:


new_file = pd.read_csv(filepath_or_buffer='./TLM_LIST (1).csv')

new_file.head()


# In[4]:


# only get the reqd part

new_file_filtered = new_file.dropna(axis=0)


# In[5]:


new_file_filtered


# In[8]:


time_data = new_file_filtered[new_file_filtered['Package'] == 'TIME']

time_data


# In[15]:


# building the output

time_result = """
BEGIN TIME

Answer
"""

for answer in list(time_data['Answer']):
    time_result += " " + str(answer)
    
time_result += "\n" + "END TIME"

time_result


# In[16]:


new_file_filtered


# In[29]:


# get hex addresses of position data

position_hex = []


for hex_addr in list(new_file_filtered['Hex Addr']):
    if new_file_filtered[new_file_filtered['Hex Addr']==hex_addr]['Mnemonic'].values[0][:8] == 'POSITION':
        position_hex.append(hex_addr)
        
position_hex


# In[31]:


position_data = new_file_filtered[new_file_filtered['Hex Addr'].isin(position_hex)]


# In[32]:


# building the output

position_result = """
BEGIN POSITION

Answer
"""

for answer in list(position_data['Answer']):
    position_result += " " + str(answer)
    
position_result += "\n" + "END POSITION"

position_result


# In[33]:


# get hex addresses of velocity data


velocity_hex = []


for hex_addr in list(new_file_filtered['Hex Addr']):
    if new_file_filtered[new_file_filtered['Hex Addr']==hex_addr]['Mnemonic'].values[0][:8] == 'VELOCITY':
        velocity_hex.append(hex_addr)
        
velocity_hex


# In[34]:


velocity_data = new_file_filtered[new_file_filtered['Hex Addr'].isin(velocity_hex)]

velocity_data


# In[35]:


# building the output


velocity_result = """
BEGIN VELOCITY

Answer
"""

for answer in list(velocity_data['Answer']):
    velocity_result += " " + str(answer)
    
velocity_result += "\n" + "END VELOCITY"

velocity_result


# In[38]:


first_line = 'stk.v.7.0'


# In[39]:


# write into the files

time_file = open('./time', 'w')

time_file.write(first_line + "\n" + time_result)

time_file.close()


# In[40]:


# write into the files


velocity_file = open('./velocity', 'w')

velocity_file.write(first_line + "\n" + velocity_result)

velocity_file.close()


# In[41]:


# write into the files


position_file = open('./position', 'w')

position_file.write(first_line + "\n" + position_result)

position_file.close()

