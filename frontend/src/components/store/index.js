// Initializing the store
import { createStore } from "redux";
import rootReducer from "reducers";

const datastore = createStore(rootReducer);

export default datastore;
