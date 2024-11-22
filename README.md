# plantshelf

Day 1
started on the backend
made plants
made locations - used generics for this

Day 2
had troubles formatting the database of plants I had generated... took an unexpectedly long time to sort. Had forgotten to put brackets after the text box in bio in the model... this meant that it cuoldnt add my data which contained a bio

decided on adding the ability to sign in with username or email - which required some research to get to work

added seeding files

created my plants - saved till last because it relied on all the others, had a lot of relationships

Day 3
Added authentication and authorization to routes. 
Created custom IsOwner permission view to ensure that users can only view their own my_plants and not anyone else's
added more errors to exceptions
in my_plants, populated the GET routes for index and show with the extra info

Day 4
had an issue working out how to generate a token and automatically sign in a user after signing up. this wasnt in my initial backend code when creating the front end code.scrutinising the code, I realised I was trying to use new_user, which wasn't an actual user saved into the database yet. So I gave a name to the save part and then used that, which was a saved user to generate the token
the error message informed me that new_user didnt have an id - which made sense because it was jsut the form information which hadnt been assigned an id yet
Implemented sass - created variables, global, etc. 
made reusable PlantInfo component which works for plants and my_plants detail pages

Day 5
Found Mantine, a component library, to add modal forms
Decided on using an icons library too for plant details
managed to add modal 'add plant to shelf' form. the difficulty is that there are so many references to other models... managed to auto set the plant species in the form data by passing the plant to the form from its parent plant detail page. location will require more thinkign
came across a problem where it wont allow me to leave a blank field for height or date last watered as intended

Day 6
// * Update
export const update = (myPlantId, formData) => {
    formData.species = formData.species.id
    formData.owner = formData.owner.id
    formData.location = formData.location.id
    return axios.put(`${BASE_URL}${myPlantId}/`, formData)
}
AxiosError
Request failed with status code 400
{"species":["Incorrect type. Expected pk value, received dict."],"owner":["Incorrect type. Expected pk value, received dict."],"location":["Incorrect type. Expected pk value, received dict."]}
This was a big prob with update form, realised through console logs and error details that it was trying to put the populated data through insterad of just the ids - fixed by altering the service function 
THEN i realised that this didnt let me edit the data in the forms, so brought it through to the useEffect()

const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            let res
            if (myPlantId) {
                res = await update(myPlantId, formData)
                close()
                fetchMyPlant()
            } else {
                res = await create(formData)
                navigate(`/my_plants/${res.data.id}`)
            }
        } catch (error) {
            console.log(error)
        }
    }
navigate away caused issues, because I was still using the same url - had to separate out fetchMyPLant with useCallback and pass it down to refresh the page after editing

Day 7/8
lots of styling and arranging to enable styling
made some changes to the backend to make it more efficient

created a DYNAMIC BOOKSHELF (aka the eponymous plantshelf). This automatically generates the required number of shelves. min three layers to give height and make it clearer that it is a bookshelf. uses remainder to calculate required shelves to finish a row, generates new rows as requried.

made all forms modal pop ups