// Initializing the store
import { createStore } from "redux";
import rootReducer from "./reducers.js";

const datastore = createStore(rootReducer);

export default datastore;
